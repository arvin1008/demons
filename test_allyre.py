import pytest
import allure

def fu(c):
    a = c+1
    return a
data = [{"test":1}]
@allure.story("测试")
@pytest.mark.parametrize("test",data)
def test6(test):
    name = test["test"]
    assert fu(name) == 2
    print("===========数据==============")

if __name__ == '__main__':
    # pytest.main()
    pytest.main(["-s"])