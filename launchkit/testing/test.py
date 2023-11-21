from launchkit import launcher_util
from launchkit.sweeper import DeterministicHyperparameterSweeper
from launchkit.logging import logger

def math_exp(variant):
    # unpack hyperparameters
    x, y = variant['x'], variant['y']
    
    # could do something with x and y here

    # simulate time / iterations
    for t in range(10):
        # log metrics
        logger.record_dict({
            'time': t,
            'pow': x ** y,
            'sum': x + y,
            'product': x * y,
        })
        x += 1
        # save all metrics to disk
        logger.dump_tabular()
        
    
if __name__ == "__main__": 
    variants=dict(
        x=[1, 2, 3],
        y=[2, 3, 4],
    )
    search_space = {}
    sweeper = DeterministicHyperparameterSweeper(
        variants,
    )
    for exp_id, variant in enumerate(sweeper.iterate_hyperparameters()):
        launcher_util.run_experiment(
            math_exp,
            variant=variant,
            exp_prefix='test',
            mode='local',
            snapshot_mode='gap_and_last',  # 'gap_and_last' saves every SNAPSHOT_GAP iterations and also the last; can also be 'all', 'last', 'gap', 'none'
            snapshot_gap=3,
        )