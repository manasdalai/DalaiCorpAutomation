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
            var driver = new ChromeDriver();
            driver.Navigate().GoToUrl("https://aws.amazon.com/");
        }
    }
}
