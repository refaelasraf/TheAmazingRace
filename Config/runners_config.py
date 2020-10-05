import asyncio

runners = [
    dict(
        name='rabbit',
        step_per_sec=3,
        start_point=0,
        do_after_step=None
    ),
    dict(
        name='turtle',
        step_per_sec=4,
        start_point=0,
        do_after_step=lambda r: asyncio.sleep(1) if r.step % 3 == 0 else asyncio.sleep(0)
    ),
    dict(
        name='snail',
        step_per_sec=1,
        start_point=10,
        do_after_step=None
    )
]
