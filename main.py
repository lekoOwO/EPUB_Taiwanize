from epubconv.epubconv import main
import sys
import asyncio

if __name__ == '__main__':
    async def _tmp():
        await main(sys.argv)
    asyncio.get_event_loop().run_until_complete(_tmp())
