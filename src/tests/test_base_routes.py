import pytest


class TestBaseRoutes:
    """

    """

    # @pytest.mark.skip()
    def test_nonexistent_route(self, client):
        res = client.get('/potato')
        assert res.status_code == 404
