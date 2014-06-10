using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using CSDemoWebApp.Engine;

namespace CSDemoWebApp
{
    public partial class _Default : Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void btnAdd_Click(object sender, EventArgs e)
        {
            try 
            {
                float res = AppEngine.Add(txbNum1.Text, txbNum2.Text);
                lblResult.Text = res.ToString();
            } catch (EngineException) {
                lblResult.Text = "Invalid input";
            }
        }

        protected void btnSub_Click(object sender, EventArgs e)
        {
            try
            {
                float res = AppEngine.Subtract(txbNum1.Text, txbNum2.Text);
                lblResult.Text = res.ToString();
            }
            catch (EngineException)
            {
                lblResult.Text = "Invalid input";
            }
        }

        protected void btnMul_Click(object sender, EventArgs e)
        {
            try
            {
                float res = AppEngine.Multiply(txbNum1.Text, txbNum2.Text);
                lblResult.Text = res.ToString();
            }
            catch (EngineException)
            {
                lblResult.Text = "Invalid input";
            }
        }

        protected void btnDiv_Click(object sender, EventArgs e)
        {
            try
            {
                float res = AppEngine.Divide(txbNum1.Text, txbNum2.Text);
                lblResult.Text = res.ToString();
            }
            catch (EngineException)
            {
                lblResult.Text = "Invalid input";
            }
        }
    }
}