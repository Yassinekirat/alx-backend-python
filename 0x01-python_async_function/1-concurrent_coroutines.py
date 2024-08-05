#!/usr/bin/python3
import asyncio
import heapq
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    heapq.heapify(delays)
    sorted_delays = [heapq.heappop(delays) for _ in range(len(delays))]
    return sorted_delays
