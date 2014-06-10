using Microsoft.Owin;
using Owin;

[assembly: OwinStartupAttribute(typeof(CSDemoWebApp.Startup))]
namespace CSDemoWebApp
{
    public partial class Startup {
        public void Configuration(IAppBuilder app) {

        }
    }
}
