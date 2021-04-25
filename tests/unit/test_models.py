from project.models import DeviceMatrix


def test_device():
    device = DeviceMatrix('devicetype', 'category', 'description', 'article', True)
    assert device.devicetype == 'devicetype'
    assert device.category == 'category'
    assert device.description == 'description'
    assert device.article == 'article'
    assert device.jws == True

