#!/usr/bin/env python3
import sys, requests, time, os, asyncio, re, random
from concurrent.futures import ThreadPoolExecutor

FAST_MODE = False
HUMAN_MODE = False

USED_BROWSERS = {}

def is_valid_url(url):
    return re.match(r"^https?://", url) is not None

def send_request(url):
    try:
        if HUMAN_MODE:
            delay = random.uniform(0.5, 2.0)
            time.sleep(delay)
            user_agents = [
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/92.0.4515.107 Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Safari/605.1.15",
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/91.0.4472.114 Safari/537.36"
            ]
            ua = random.choice(user_agents)
            USED_BROWSERS[ua] = USED_BROWSERS.get(ua, 0) + 1
            headers = {"User-Agent": ua}
        else:
            headers = {"User-Agent": "Mozilla/5.0"}
        timeout = 3 if FAST_MODE else 10
        response = requests.get(url, timeout=timeout, headers=headers)
        return response.status_code == 200
    except Exception:
        return False

async def run_requests(executor, total_times, url):
    loop = asyncio.get_event_loop()
    tasks = [loop.run_in_executor(executor, send_request, url) for _ in range(total_times)]
    completed = 0
    results = []
    for fut in asyncio.as_completed(tasks):
        result = await fut
        results.append(result)
        completed += 1
        progress = (completed / total_times) * 100
        filled_len = int(30 * completed / total_times)
        bar = "#" * filled_len + "-" * (30 - filled_len)
        sys.stdout.write(f"\rProgress: [{bar}] {progress:.2f}% complete")
        sys.stdout.flush()
    print()
    return total_times, sum(results)

async def run_requests_rate(executor, total_times, url, rate):
    req_count = 0
    success_count = 0
    loop = asyncio.get_event_loop()
    while req_count < total_times:
        batch = min(rate, total_times - req_count)
        tasks = [loop.run_in_executor(executor, send_request, url) for _ in range(batch)]
        results = await asyncio.gather(*tasks)
        req_count += batch
        success_count += sum(results)
        progress = (req_count / total_times) * 100
        filled_len = int(30 * req_count / total_times)
        bar = "#" * filled_len + "-" * (30 - filled_len)
        sys.stdout.write(f"\rProgress: [{bar}] {progress:.2f}% complete")
        sys.stdout.flush()
    print()
    return req_count, success_count

def main():
    if len(sys.argv) == 2 and sys.argv[1].lower() == "help":
        print("Usage: surge <url> <times> <mode> [rate] (optional)")
        print("  url   - Target URL (must start with http:// or https://)")
        print("  times - Number of requests to send")
        print("  mode  - Execution mode: F for Fast, H for Human, R for Rate-limited")
        print("  rate  - Requests per second limit (max 50), applies only in R mode")
        print("Examples:")
        print("surge https://example.com 100 R 10")
        print("surge https://example.com 100 H")
        return

    if len(sys.argv) < 4:
        print("Usage: surge <url> <times> <mode> [rate] (optional)")
        return

    url = sys.argv[1]
    total_times = int(sys.argv[2])
    
    if not is_valid_url(url):
        print("Please enter a valid URL")
        return

    mode = sys.argv[3].upper()
    rate = None
    input_rate_str = None
    if mode == "R":
        if len(sys.argv) < 5:
            print("Usage: surge <url> <times> R <rate>")
            return
        input_rate_str = sys.argv[4]
        try:
            rate = int(input_rate_str)
            if rate > 50:
                rate = 50
        except ValueError:
            print("Please enter a valid rate")
            return

    global FAST_MODE, HUMAN_MODE
    if mode == "H":
        HUMAN_MODE = True
        FAST_MODE = False
    elif mode == "F":
        FAST_MODE = True
        HUMAN_MODE = False
    elif mode == "R":
        FAST_MODE = True
        HUMAN_MODE = False
    else:
        print("Unknown mode, please use F, H, or R")
        return

    print(f"Website to test: {url}")
    print(f"Number of requests: {total_times}")
    mode_str = "Rate-limited mode (R)" if mode == "R" else ("Human mode (H)" if HUMAN_MODE else "Fast mode (F)")
    print(f"Execution mode: {mode_str}")
    if mode == "R":
        print("Max rate: " + input_rate_str)
    confirm = input("Confirm the above information (Y to continue, any other key to cancel): ")
    if confirm.upper() != "Y":
        print("Operation canceled")
        return

    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=50) as executor:
        if mode == "R":
            req_count, success_count = asyncio.run(run_requests_rate(executor, total_times, url, rate))
        else:
            req_count, success_count = asyncio.run(run_requests(executor, total_times, url))
    
    print(f"\nCompleted {req_count} requests, {success_count} succeeded")
    elapsed = round(time.time() - start_time, 2)
    print(f"Total execution time: {elapsed} seconds")
    
if __name__ == "__main__":
    main()
