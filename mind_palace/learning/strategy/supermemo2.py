import random

from decimal import Decimal
from datetime import datetime, timedelta

from mind_palace.learning.strategy.base import BaseLearningStrategy


class SuperMemo2LearningStrategy(BaseLearningStrategy):

    def generate_learning_queue(self, root_node):
        queue = list(root_node.get_descendants(include_self=True).order_by(
            'learning_statistics__next_repetition'
        ).values_list('id', flat=True))
        random.shuffle(queue)
        return queue

    def study_node(self, node_learning_stats, rating):
        """
        Handle node repetition using supermemo2 strategy.

        https://www.supermemo.com/ru/archives1990-2015/english/ol/sm2
        This is implementation of algorithm described in the link.
        Repetition strategy calculates optimal next repetition datetime of some data based on
        user repetition rating(subjective repetition quality rating).
        """

        if rating < 3:
            # if repetition is not positive e.g. repetition rating lower that 3, set positive
            # repetition in a row to 0 and repeat this node next day.
            node_learning_stats.positive_repetitions_in_row = 0
            node_learning_stats.easiness = node_learning_stats.easiness
            node_learning_stats.interval = 1

        else:
            q = rating
            new_easiness = node_learning_stats.easiness + Decimal(
                (0.1 - (5 - q) * (0.08 + (5 - q) * 0.02))
            )
            node_learning_stats.easiness = new_easiness.quantize(Decimal('1.0'))

            # User rated repetition as positive
            if node_learning_stats.positive_repetitions_in_row == 0:
                # if this is first positive repetition repeat this node tomorrow again
                node_learning_stats.interval = 1

            elif node_learning_stats.positive_repetitions_in_row == 1:
                # According to supermemo2 must be 6 days
                node_learning_stats.interval = 4
            else:
                node_learning_stats.interval = round(
                    node_learning_stats.interval * node_learning_stats.easiness, 1
                )

            node_learning_stats.positive_repetitions_in_row += 1

        node_learning_stats.next_repetition = (
                node_learning_stats.last_repetition + timedelta(
                    days=float(node_learning_stats.interval)
                )
        )
        node_learning_stats.last_repetition = datetime.utcnow()
        node_learning_stats.average_rate = (
            ((node_learning_stats.repetitions * node_learning_stats.average_rate) + rating) /
            (node_learning_stats.repetitions + 1)
        )
        node_learning_stats.repetitions += 1
        node_learning_stats.save()
