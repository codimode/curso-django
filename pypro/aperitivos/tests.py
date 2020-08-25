import pytest
from django.urls import reverse

from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:video', args=('motivacao',)))


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo_video(resp):
    assert_contains(resp, 'All Going To Die')
    
    
def test_conteudo_video(resp):
    assert_contains(resp, '<iframe src="https://player.vimeo.com/video/292711054?title=0&byline=0&portrait=0&badge=0"')
