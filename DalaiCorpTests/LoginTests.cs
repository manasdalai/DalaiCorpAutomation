using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using DalaiCorpAutomation;

namespace DalaiCorpTests
{
    [TestClass]
    public class LoginTests
    {
        [TestMethod]
        public void Admin_User_Can_Login()
        {
            LoginPage.GoTo();
           // LoginPage.SignUpAs("Admin").WithPassword("Password").Login();
            //Assert.IsTrue(DashBoardPage.IsAt, "Failed to Login");
        }
    }
}
