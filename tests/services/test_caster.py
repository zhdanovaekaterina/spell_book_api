import pytest

from app.core import CasterModel, NotFoundException

dict_caster = [({
    'name': 'Player1',
    'classes': [{
        'alias': 'wizard',
    }],
    'stats': {
        'intelligence': 16,
        'wisdom': 10,
        'charisma': 10,
    }
})]


# todo: зависит от тестов модели заклинателя
@pytest.mark.dependency(name="create")
@pytest.mark.parametrize("data", dict_caster)
def test_create(caster_service, data):
    repo = caster_service.repository

    # создадим персонажа
    caster_id = caster_service.create(**data)
    assert caster_id
    assert len(repo.caster)

    # проверим что он есть в репозитории
    caster_from_repo = repo.caster[0]
    assert type(caster_from_repo) is CasterModel
    assert caster_from_repo.id == caster_id

    # создадим еще одного
    another_caster_id = caster_service.create(**data)
    another_caster_from_repo = repo.caster[1]
    assert another_caster_from_repo.id == another_caster_id


@pytest.mark.dependency(depends=["create"])
def test_get_wrong(caster_service):
    with pytest.raises(NotFoundException):
        caster_service.get(3)


@pytest.mark.dependency(depends=["create"])
def test_delete_wrong(caster_service):
    with pytest.raises(NotFoundException):
        caster_service.delete(3)


@pytest.mark.dependency(name="get_existing", depends=["create"])
@pytest.mark.parametrize("data", dict_caster)
def test_get_existing(caster_service, data):
    repo = caster_service.repository
    len_before = len(repo.caster)

    # получим второго персонажа
    caster = caster_service.get(2)
    assert type(caster) is dict
    assert caster.get('id') == 2
    assert len(repo.caster) == len_before

    assert (caster.get('stats').get('intelligence')
            == data.get('stats').get('intelligence'))


@pytest.mark.dependency(depends=["get_existing"])
def test_delete_existing(caster_service):
    repo = caster_service.repository
    len_before = len(repo.caster)

    # удалим первого
    caster_service.delete(1)
    assert len(repo.caster) == len_before-1

    # получим второго после удаления первого
    left_caster = caster_service.get(2)
    assert left_caster
    assert left_caster['id'] == 2
