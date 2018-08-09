using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using DalaiCorpAutomation;

namespace DalaiCorpTests
{
    [TestClass]
    public class UnitTest1
    {
        [TestMethod]
        public void TestMethod1()
        {
            var c = new Class1();
            c.Go();
        }
    }
}
