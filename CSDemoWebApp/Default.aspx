<%@ Page Title="Home Page" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="Default.aspx.cs" Inherits="CSDemoWebApp._Default" %>

<asp:Content ID="BodyContent" ContentPlaceHolderID="MainContent" runat="server">

    <div class="jumbotron">
        <span><asp:TextBox ID="txbNum1" runat="server" Width="97px"></asp:TextBox></span>
        <span><asp:TextBox ID="txbNum2" runat="server" Width="97px"></asp:TextBox></span>
        <br />
        <asp:Button ID="btnAdd" runat="server" Text="Add" OnClick="btnAdd_Click" />
        <asp:Button ID="btnSub" runat="server" Text="Subtract" OnClick="btnSub_Click" />
        <asp:Button ID="btnMul" runat="server" Text="Multiply" OnClick="btnMul_Click" />
        <asp:Button ID="btnDiv" runat="server" Text="Divide" OnClick="btnDiv_Click" />
        <br />
        <asp:Label ID="lblResult" runat="server" Text=""></asp:Label>
    </div>
</asp:Content>
