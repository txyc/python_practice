# 这里仅针对unittest的做简单的整理说明，unittest框架的核心概念如下：
# 1、testcase——测试用例，继承unittest.TestCase类，可使用unittest.mian()来执行用例
# 2、testsuite——测试套，创建unittest.TestSuite()实例，然后使用addTest()添加用例到测试套中
# 3、testrunner——测试运行套件，创建unittest.TextTestRunner()实例，然后通过run()方法运行测试套任务
# 4、testloader——测试加载套件，创建unittest.TestLoader()等实例，然后通过discover()获取需要执行的测试用例
# 5、testfixture——测试夹具套件，主要用于对测试环境的前置搭建(setup)和后置还原(teardown)
#   测试夹具中控制级别分为函数级、类级、模块级，其中：
#   函数级——def setUp()/tearDown():每个测试函数执行前都会执行setUp，执行后都会执行tearDown
#   类级——def setUpClass()/tearDownClass():测试类执行前都会执行setUpClass，执行后都会执行tearDownClass
#   模块级——def setUpModule()/tearDownModule():测试模块执行前都会执行setUpModule，执行后都会执行tearDownModule
# 6、还可以配合HTMLTestRunner和BeautifulReport来完成测试报告的呈现
#   其中HTMLTestRunner的报告相对简单，而且原始版本仅支持2.x需要做部分修改，修改方法可参考：https://blog.csdn.net/cheng_jeff/article/details/121238308
#   BeautifulReport的报告呈现要更为美观，python3.x版本可直接使用