import asyncio
from datetime import timedelta
import rio
import rio_jobs


# Regular code to create your Rio app. This one is just an example that displays
# a static text.
class MyRoot(rio.Component):
    def build(self) -> rio.Component:
        return rio.Text(
            "Hello, world!",
            justify="center",
        )


# Create a scheduler
scheduler = rio_jobs.JobScheduler()


# Create a function for the scheduler to run. This function can by synchronous
# or asynchronous. The `@scheduler.schedule` decorator adds the function to the
# scheduler.
@scheduler.job(
    timedelta(hours=1),
)
async def my_job() -> timedelta:
    # Do some work here
    print("Working hard!")
    await asyncio.sleep(100)

    # Optionally reschedule the job. This can return
    #
    # - a `datetime` object to schedule the job at a specific time
    # - a `timedelta` object to wait for a specific amount of time
    # - literal `"never"` to stop the job
    #
    # ... or simply return nothing to keep running the job at the configured
    # interval.
    return timedelta(hours=3)


# Pass the scheduler to the Rio app. Since Rio's extension interface isn't
# stable yet, we'll add the extension manually after the app has been created.
app = rio.App(
    build=MyRoot,
)

app._add_extension(scheduler)

# Run your Rio app as usual. If you want to use `rio run`, remove this line
app.run_in_browser()
