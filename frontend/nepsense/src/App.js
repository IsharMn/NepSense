import React, { Component } from 'react';
import axios from 'axios';

class App extends Component{
	state = {
		todos: []
	};

	componentDidMount(){
	this.getStocks();
	}

	getStocks(){
		axios.get('http://127.0.0.1:8000/api')
		.then(res => {
			this.setState({todos: res.data});
		})
		.catch(err => {
			console.log(err);
		})
	}

	render(){
		return (
			<div>
				<table>
					{this.state.todos.map(obj => (
						<tr key={obj.id}>
							<td>{obj.company}</td>
							<td>{obj.transno}</td>
							<td>{obj.prevclosep}</td>
							<td>{obj.closep}</td>
							<td>{obj.diff}</td>
						</tr>
					))}
				</table>
			</div>
		)
	}
}

export default App;