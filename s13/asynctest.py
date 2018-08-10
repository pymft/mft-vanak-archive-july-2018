import asyncio

async def fib(n):
    N=n
    print("fib({n})".format(n=N))
    if n in (1, 2):
        print("fib({n}) = {b}".format(n=N, b=1))
        return 1
    a, b = 1, 1
    n -= 2
    while n:
        a, b = b, a+b
        n -= 1
        if n % 1000 == 0:
            await asyncio.sleep(0.0001)
    print("fib({n}) = {b}".format(n=N, b=b))
    return b

async def main(loop):

    t1 = loop.create_task(fib(1200))
    t2 = loop.create_task(fib(4000))
    t3 = loop.create_task(fib(1000))
    t4 = loop.create_task(fib(150))S

    await asyncio.wait([t1,t2, t3, t3])
    return t1, t2, t3, t4

if __name__ == '__main__':
    try:
        loop = asyncio.get_event_loop()
        r1, r2, r3, r4= loop.run_until_complete(main(loop))
        print(r1._result)
        print (r1)
    except:
        print ("something went wrong!")
    finally:
        loop.close()
