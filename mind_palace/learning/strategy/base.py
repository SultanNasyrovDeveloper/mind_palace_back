

class BaseLearningStrategy:
    """
    Base learning strategy. Defines common to all learning strategies interface.
    """

    def generate_learning_queue(self, root_node):
        raise NotImplementedError

    def handle_repetition(self, node_learning_stats, repetition_rating):
        """
        Handle user mind palace node repetition.

        Args:
            node_learning_stats: Mind palace node learning statistics.
            repetition_rating: New repetition rating.
        """
        raise NotImplementedError
