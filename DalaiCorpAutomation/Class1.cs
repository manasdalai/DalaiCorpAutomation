using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium;

namespace DalaiCorpAutomation
{
    public class Class1
    {
        public void Go()
        {
           
            IWebDriver driver = new ChromeDriver(@"C:\Manas Stuffs\Trainings and Tutorials\AutomationFramework\UsingCsharpVisualStudio\DalaiCorpAutomation\packages\Selenium.WebDriver.ChromeDriver.2.40.0\driver\win32");
            
            driver.Navigate().GoToUrl("www.google.com");


        }
    }
}
