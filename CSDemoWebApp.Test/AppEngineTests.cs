using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using NUnit.Framework;
using CSDemoWebApp.Engine;

namespace CSDemoWebApp.Test
{

    [TestFixture]
    public class AppEngineTests
    {
        [TestCase]
        public void AdditionTest()
        {
            float res = AppEngine.Add("45", "6");
            Assert.AreEqual(res, 51);
            res = AppEngine.Add("-7", "-6");
            Assert.AreEqual(res, -13);
            Assert.Throws<EngineException>(() => AppEngine.Add("", "6"));
            Assert.Throws<EngineException>(() => AppEngine.Add("13", ""));
            Assert.Throws<EngineException>(() => AppEngine.Add("1", "text"));
            Assert.Throws<EngineException>(() => AppEngine.Add("text", "7"));
        }

        [TestCase]
        public void SubtractionTest()
        {
            float res = AppEngine.Subtract("45", "6");
            Assert.AreEqual(res, 39);
            res = AppEngine.Subtract("-7", "-6");
            Assert.AreEqual(res, -1);
            Assert.Throws<EngineException>(() => AppEngine.Subtract("", "6"));
            Assert.Throws<EngineException>(() => AppEngine.Subtract("13", ""));
            Assert.Throws<EngineException>(() => AppEngine.Subtract("1", "text"));
            Assert.Throws<EngineException>(() => AppEngine.Subtract("text", "7"));
        }

        [TestCase]
        public void MultiplicationTest()
        {
            float res = AppEngine.Multiply("45", "6");
            Assert.AreEqual(res, 270);
            res = AppEngine.Multiply("-7", "-6");
            Assert.AreEqual(res, 42);
            Assert.Throws<EngineException>(() => AppEngine.Multiply("", "6"));
            Assert.Throws<EngineException>(() => AppEngine.Multiply("13", ""));
            Assert.Throws<EngineException>(() => AppEngine.Multiply("1", "text"));
            Assert.Throws<EngineException>(() => AppEngine.Multiply("text", "7"));
        }

        [TestCase]
        public void DivisionTest()
        {
            float res = AppEngine.Divide("45", "6");
            Assert.AreEqual(res, 7.5);
            res = AppEngine.Divide("-18", "-6");
            Assert.AreEqual(res, 3);
            Assert.Throws<EngineException>(() => AppEngine.Divide("13", "0"));
            Assert.Throws<EngineException>(() => AppEngine.Divide("", "6"));
            Assert.Throws<EngineException>(() => AppEngine.Divide("13", ""));
            Assert.Throws<EngineException>(() => AppEngine.Divide("1", "text"));
            Assert.Throws<EngineException>(() => AppEngine.Divide("text", "7"));
        }
    }
}
