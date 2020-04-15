import React from 'react';
import { Table, Tabs } from 'antd';
import axios from 'axios';
import Button from 'react-bootstrap/Button';
import 'antd/dist/antd.css';
import { CarryOutTwoTone, CalendarTwoTone } from '@ant-design/icons'

const TabPane = Tabs.TabPane;


class Events extends React.Component {
    constructor(props) {
        super(props);
        this.pastColumns = [
            {
                title: 'Event',
                dataIndex: 'name',
                key: 'name',
                render: text => <a>{text}</a>
            },
            {
                title: 'Start Time',
                dataIndex: 'start_time',
                key: 'start_time',
            },
            {
                title: 'End Time',
                dataIndex: 'end_time',
                key: 'end_time',
            },
            {
                title: 'Description',
                dataIndex: 'description',
                key: 'description',
            },
        ];
        this.upcomingColumns = [
            {
                title: 'Event',
                dataIndex: 'name',
                key: 'name',
                render: text => <a>{text}</a>
            },
            {
                title: 'Start Time',
                dataIndex: 'start_time',
                key: 'start_time',
            },
            {
                title: 'End Time',
                dataIndex: 'end_time',
                key: 'end_time',
            },
            {
                title: 'Description',
                dataIndex: 'description',
                key: 'description',
            },
            {
                title: 'Action',
                key: 'x',
                render: (text, record) => (
                    <span>
                        <Button variant="success">Attend</Button>
                    </span>
                ),
            },
        ];

        this.pastEvents = [];
        this.upcomingEvents = [];

        this.state = {
            pastColumns: this.pastColumns,
            upcomingColumns: this.upcomingColumns,
            pastEvents: this.pastEvents,
            upcomingEvents: this.upcomingEvents,
        };

    }

    // Times come in as UTC and are converted to users local time
    // NOTE: Sorting is based off of the key (id) value passed from the django event object rather than the date and time of the event
    organize_events = function (json) {
        var i, ended = false, past = [], upcoming = [];
        for (i = 0; i < json.length; i++) {
            var d = new Date(json[i]["start_time"]);
            json[i]["start_time"] = d.toLocaleString('en-US', {
                dateStyle: "full", timeStyle: "long", hour12: true
            });
            d = new Date(json[i]["end_time"]);
            ended = d.getTime() < Date.now()
            json[i]["end_time"] = d.toLocaleString('en-US', {
                dateStyle: "full", timeStyle: "long", hour12: true
            });
            if (ended) {
                past.push(json[i])
            }
            else {
                upcoming.push(json[i])
            }
        }
        return [upcoming, past]
    }

    componentDidMount() {
        this.updateEventsData()
    }

    updateEventsData = value => {
        const url = 'http://localhost:8000/api/events/';
        axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
        axios.defaults.xsrfCookieName = "csrftoken";
        axios.defaults.headers = {
            "Content-Type": "application/json",
            Authorization: `Token ${this.props.token}`
        };
        axios({
            method: 'get',
            url: url,
            auth: {
                username: "herrab",
                password: "admin"
            }
        })
            .then(res => {
                console.log(res.data[0]["key"])
                var events = this.organize_events(res.data) //
                this.setState({
                    upcomingEvents: events[0],
                    pastEvents: events[1]
                })
            })
            .catch(err => console.log(err));
    }

    render() {
        return (
            <div>
                <Tabs defaultActiveKey="1">
                    <TabPane tab={<span><CalendarTwoTone />Upcoming Events</span>} key="1">
                        <div>
                            <Table
                                columns={this.state.upcomingColumns}
                                dataSource={this.state.upcomingEvents}
                            />
                        </div>
                    </TabPane>
                    <TabPane tab={<span><CarryOutTwoTone />Past Events</span>} key="2">
                        <div>
                            <Table
                                columns={this.state.pastColumns}
                                dataSource={this.state.pastEvents}
                            />
                        </div>
                    </TabPane>
                </Tabs>
            </div >
        );
    }
}
export default Events;