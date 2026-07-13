from auctionlab.research.experiments.observation_log import ObservationLog


class ExperimentRunner:

    def run(
        self,
        snapshots,
        experiment,
    ) -> ObservationLog:

        log = ObservationLog()

        for snapshot in snapshots:

            observation = experiment.run(snapshot)

            if observation is not None:
                log.add(observation)

        return log