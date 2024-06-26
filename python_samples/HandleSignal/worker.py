import asyncio

from temporalio.client import Client
from temporalio.worker import Worker
from signalwf import MySignalWorkflow

async def main():
	client = await Client.connect("localhost:7233")
	worker = Worker(client, task_queue="signal_tq", workflows=[MySignalWorkflow])
	await worker.run()

if __name__=="__main__":
	asyncio.run(main())

