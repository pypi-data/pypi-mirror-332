import asyncio
import ssl
import dns.message
import dns.query
import httpx
from cachetools import TTLCache
from .exceptions import DNSQueryError
from .logging import logger

class DNSResolver:
    """
    A resolver for querying DNS over HTTPS (DoH) and DNS over TLS (DoT).

    This class supports both synchronous and asynchronous DNS queries, with
    retries, caching, and logging for better performance and reliability.

    Attributes:
        doh_server (str): The URL of the DoH server (default: "https://dns.google/dns-query").
        dot_server (str): The address of the DoT server (default: "1.1.1.1").
        dot_port (int): The port for DoT server (default: 853).
        mtls_server (str): The address of the mTLS server, if applicable.
        certfile (str): Path to the client certificate for mTLS, if applicable.
        keyfile (str): Path to the client key for mTLS, if applicable.
        retries (int): Number of retries on query failure (default: 3).
        cache (TTLCache): A cache for storing DNS query results to optimize repeated queries.

    Methods:
        __init__: Initializes the resolver with given settings.
        _query_doh: Performs a DNS query over HTTPS (DoH) asynchronously.
        _query_dot: Performs a DNS query over TLS (DoT) asynchronously.
        query: Resolves DNS queries using the specified protocol with retries, caching, and logging.
    """

    def __init__(self,
                 doh_server="https://dns.google/dns-query",
                 dot_server="1.1.1.1", dot_port=853,
                 mtls_server=None, certfile=None, keyfile=None,
                 cache_size=100, cache_ttl=300, retries=3):
        """
        Initializes the DNSResolver instance with the provided server addresses and configuration.

        Args:
            doh_server (str): The URL of the DoH server (default: "https://dns.google/dns-query").
            dot_server (str): The IP address of the DoT server (default: "1.1.1.1").
            dot_port (int): The port for the DoT server (default: 853).
            mtls_server (str, optional): The address of the mTLS server (default: None).
            certfile (str, optional): Path to the mTLS client certificate (default: None).
            keyfile (str, optional): Path to the mTLS client key (default: None).
            cache_size (int): Maximum size of the cache (default: 100).
            cache_ttl (int): TTL in seconds for cached DNS responses (default: 300).
            retries (int): Number of retry attempts for failed queries (default: 3).
        """
        self.doh_server = doh_server
        self.dot_server = dot_server
        self.dot_port = dot_port
        self.mtls_server = mtls_server
        self.certfile = certfile
        self.keyfile = keyfile
        self.retries = retries

        # Cache for storing DNS responses (TTL-based)
        self.cache = TTLCache(maxsize=cache_size, ttl=cache_ttl)

    async def _query_doh(self, domain: str, record_type: str):
        """
        Performs a DNS query over HTTPS (DoH) asynchronously, with caching, retries, and logging.

        Args:
            domain (str): The domain to query.
            record_type (str): The type of DNS record to request (e.g., 'A', 'AAAA').

        Returns:
            list: The DNS response, which is a list of DNS answer records.

        Raises:
            DNSQueryError: If the DoH query fails after the specified number of retries.
        """
        cache_key = f"doh:{domain}:{record_type}"
        if cache_key in self.cache:
            logger.info(f"Cache hit for {cache_key}")
            return self.cache[cache_key]

        query = dns.message.make_query(domain, record_type)

        for attempt in range(1, self.retries + 1):
            try:
                async with httpx.AsyncClient() as client:
                    response = await client.post(
                        self.doh_server,
                        data=query.to_wire(),
                        headers={"Content-Type": "application/dns-message"},
                    )
                    if response.status_code == 200:
                        result = dns.message.from_wire(response.content).answer
                        self.cache[cache_key] = result
                        logger.info(f"DoH query success for {domain} (attempt {attempt})")
                        return result
                    logger.warning(f"DoH query failed for {domain} (attempt {attempt})")

            except Exception as e:
                logger.error(f"DoH query error: {e} (attempt {attempt})")

        raise DNSQueryError(f"Failed DoH query after {self.retries} attempts")

    async def _query_dot(self, domain: str, record_type: str):
        """
        Performs a DNS query over TLS (DoT) asynchronously, with caching, retries, and logging.

        Args:
            domain (str): The domain to query.
            record_type (str): The type of DNS record to request (e.g., 'A', 'AAAA').

        Returns:
            list: The DNS response, which is a list of DNS answer records.

        Raises:
            DNSQueryError: If the DoT query fails after the specified number of retries.
        """
        cache_key = f"dot:{domain}:{record_type}"
        if cache_key in self.cache:
            logger.info(f"Cache hit for {cache_key}")
            return self.cache[cache_key]

        query = dns.message.make_query(domain, record_type)
        ssl_context = ssl.create_default_context()

        for attempt in range(1, self.retries + 1):
            try:
                response = await asyncio.to_thread(
                    dns.query.tls, query, self.dot_server, self.dot_port, ssl_context
                )
                self.cache[cache_key] = response.answer
                logger.info(f"DoT query success for {domain} (attempt {attempt})")
                return response.answer

            except Exception as e:
                logger.error(f"DoT query error: {e} (attempt {attempt})")

        raise DNSQueryError(f"Failed DoT query after {self.retries} attempts")

    def query(self, domain: str, record_type: str = "A", protocol: str = "doh", async_mode: bool = False):
        """
        Resolves a DNS query for the given domain using the specified protocol (DoH or DoT), with retries,
        caching, and logging. Returns a coroutine if `async_mode` is True, or directly executes the query
        in sync mode.

        Args:
            domain (str): The domain to resolve.
            record_type (str): The type of DNS record to request (default is 'A').
            protocol (str): The DNS protocol to use ('doh' or 'dot'). Default is 'doh'.
            async_mode (bool): Whether to perform the query asynchronously (default is False).

        Returns:
            coroutine or list: If `async_mode` is True, a coroutine object is returned, which resolves to
                                the DNS response when awaited. If `async_mode` is False, the DNS response
                                list is returned directly.

        Raises:
            ValueError: If an invalid protocol is provided.
        """
        logger.info(f"Resolving {domain} using {protocol} (Async: {async_mode})")

        if protocol == "doh":
            coroutine = self._query_doh(domain, record_type)
        elif protocol == "dot":
            coroutine = self._query_dot(domain, record_type)
        else:
            raise ValueError("Invalid protocol. Choose 'doh' or 'dot'.")

        return coroutine if async_mode else asyncio.run(coroutine)
