import pytest

from mind_palace_back.palace.node.models import MindPalaceNode


@pytest.mark.django_db
def test_subtree(api_client):
    root_node = MindPalaceNode.objects.create(name='Test root node')
    for i in range(5):
        child = MindPalaceNode.objects.create(name=f'Child {i}', parent=root_node)
    MindPalaceNode.objects.create(name='Grand', parent=child)
    response = api_client.get(f'/api/v1/palace/palaces/tree/?root={root_node.id}&depth=2')
    print(response.data)
    assert True
