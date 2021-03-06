import React from "react";
import { Layout, Menu } from "antd";
import { connect } from "react-redux";
import axios from "axios";
import { NavLink, Route } from "react-router-dom";
import ChatUI from "./ChatUI";

const { SubMenu } = Menu;
const { Content, Sider } = Layout;

class ChatPage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      currentChat: "",
      chats: [
        {
          key: "",
          name: "",
        },
      ],
      friends: [
        {
          key: "",
          name: "",
        },
      ],
    };

    this.getCurrChats();
    // this.getFriends();
  }

  componentDidUpdate() {
    if (!this.props.isAuthenticated) {
      this.props.history.push("/login");
    }
  }

  getFriends = () => {
    const url = `${process.env.REACT_APP_HOST_IP_ADDRESS}/api/get-friends/`;
    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
    axios.defaults.xsrfCookieName = "csrftoken";
    axios.defaults.headers = {
      "Content-Type": "application/json",
      Authorization: `Token ${this.props.token}`,
    };
    axios
      .get(url)
      .then((response) => response.data)
      .then((data) => {
        console.log(data);
        this.setState({ friends: data });
      });
  };

  getNewChat = (value) => {
    const url = `${process.env.REACT_APP_HOST_IP_ADDRESS}/api/chats/create/`;
    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
    axios.defaults.xsrfCookieName = "csrftoken";
    axios.defaults.headers = {
      "Content-Type": "application/json",
      Authorization: `Token ${this.props.token}`,
    };
    axios
      .post(url, { usernames: [this.props.username, value] })
      .then((response) => response.data)
      .then((data) => {
        console.log(data);
        this.setState({
          currentChat: data["pk"],
        });
        this.setState((state) => {
          return [...state.currChats, { key: data["pk"], name: value }];
        });
      });
  };

  getCurrChats = () => {
    const url = `${process.env.REACT_APP_HOST_IP_ADDRESS}/api/get-chats/`;
    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
    axios.defaults.xsrfCookieName = "csrftoken";
    axios.defaults.headers = {
      "Content-Type": "application/json",
      Authorization: `Token ${this.props.token}`,
    };
    axios
      .get(url)
      .then((response) => response.data)
      .then((data) => {
        this.setState({
          chats: data,
        });
      });
  };

  showChat = (value) => {
    this.setState({
      currentChat: value,
    });
  };

  render() {
    return (
      <Layout>
        <Sider>
          <Menu
            mode="inline"
            defaultOpenKeys={["sub1"]}
            style={{ height: "100%", borderRight: 0 }}
          >
            <SubMenu key="sub1" title="Current Chats">
              {this.state.chats.map((chat) => (
                <Menu.Item key={chat.key}>
                  <NavLink to={`/chat/${chat.key}`}>
                    {chat.name}
                    {chat.key}
                  </NavLink>
                </Menu.Item>
              ))}
            </SubMenu>
            <SubMenu key="sub2" title="Friends">
              {this.state.friends.map((friend) => (
                <Menu.Item
                  key={friend.key}
                  onClick={() => this.getNewChat(friend.name)}
                >
                  {friend.name}
                </Menu.Item>
              ))}
            </SubMenu>
          </Menu>
        </Sider>
        <Content>
          <Route exact path={`/chat/:chatId`} component={ChatUI} />
        </Content>
      </Layout>
    );
  }
}

const mapStateToProps = (state) => ({
  token: state.auth.token,
  username: state.auth.username,
  isAuthenticated: state.auth.token !== null,
  // chats: state.message.chats,
});

export default connect(mapStateToProps)(ChatPage);
