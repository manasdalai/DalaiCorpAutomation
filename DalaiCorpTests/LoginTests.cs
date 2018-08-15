using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using DalaiCorpAutomation;

namespace DalaiCorpTests
{
    [TestClass]
    public class LoginTests
    {
        [TestInitialize]
        public void Init()
        {
            Driver.Initialize();
        }

        [TestMethod]
        public void Admin_User_Can_Login()
        {
            LoginPage.GoTo();
            LoginPage.LoginAs("Admin").WithPassword("Password").Login();
            //Assert.IsTrue(DashBoardPage.IsAt, "Failed to Login");
        }

        [TestCleanup]
        
    }
}
