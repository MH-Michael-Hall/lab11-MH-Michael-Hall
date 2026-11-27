# Intermediate programming practice: async and sockets.
#
# For EACH problem, work out your problem-solving OUTLINE first, then implement it (you
# may use an AI assistant to help - see the README). The async parts must actually run
# their work CONCURRENTLY (that's the whole point), not one after another.
#
# Do not rename the functions - the tests use these names.

import asyncio
import socket


async def gather_doubled(numbers):
    # Outline (write your plan here first):
    #   define an async function that accepts a number and returns the number doubled
    #   create list of coroutines of the function for each number in input list
    #   calculate results of coroutines concurrently using asyncio.gather
    #   return results
    #
    # Instructions (Part 1, async): run one async task per number that returns n * 2, all
    #   CONCURRENTLY with asyncio.gather, and return the results as a list in the same
    #   order as `numbers`.
    async def doubled(n):
        return n*2
    
    results = await asyncio.gather(*(doubled(n) for n in numbers))
    return results


async def fastest(jobs):
    # Outline:
    #   define async function that sleeps for a delay and returns the job label
    #   create a list of coroutines of the function for a list of labels and delays
    #   run the coroutines conocurrently
    #   use asyncio.as_completed to order results in completion order
    #   return first completed result
    #
    # Instructions (Part 2, async): `jobs` is a list of (label, delay) pairs. Start them all
    #   concurrently - each one just does `await asyncio.sleep(delay)` - and return the
    #   label of the FIRST job to finish. (Hint: asyncio.as_completed.)

    async def do_job(job, delay):
        await asyncio.sleep(delay)
        return job
    
    tasks = [asyncio.create_task(do_job(j,d)) for j,d in jobs]
    results = []

    for task in asyncio.as_completed(tasks):
        results += await task

    return results[0]


def echo_once(host, port, message):
    # Outline:
    #   create client socket
    #   connect to host
    #   encode message
    #   send message
    #   receive reply
    #   decode reply
    #   return decoded reply
    #
    # Instructions (Part 3, sockets): open a TCP socket and connect to (host, port). Send
    #   `message` (encode it to bytes first), receive the server's reply, and return it
    #   as a string. (Hint: socket.socket, .connect, .sendall, .recv, .decode.)
    with socket.socket() as client:
        client.connect((host,port))
        client.sendall(message.encode())
        reply = client.recv(1024)
        return reply.decode()


def main():
    # Optional scratch space - try the async parts here, e.g.:
    # print(asyncio.run(gather_doubled([1, 2, 3, 4])))   # [2, 4, 6, 8]
    # print(asyncio.run(fastest([("A", 0.06), ("B", 0.02), ("C", 0.04)])))
    pass


if __name__ == "__main__":
    main()
