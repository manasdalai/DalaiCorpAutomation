using DalaiCorpAutomation;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DalaiCorpAutomation
{
    public class LoginPage
    {
        public static void GoTo()
        {
            Driver.Instance.Navigate().GoToUrl("https://aws.amazon.com/");
            
        }

        public static LoginCommand LoginAs(string userName)
        {
            return new LoginCommand(userName);
        }
    }
}


public class LoginCommand
{
    private readonly string userName;
    private string password;

    public LoginCommand(string userName)
    {
        this.userName = userName;
    }

    public LoginCommand WithPassword(string password)
    {
        this.password = password;
        return this;
    }

    public void Login()
    {
        var loginInput = Driver.Instance.FindElement(By.Id("aws-nav-cta-button"));
        loginInput.Click();


    }
}