'use strict';

const el = React.createElement;

class Burger extends React.Element {
  constructor(props) {
    super(props);
    this.state = { clicked: false };
  }

  render() {
    return (
      <button>

      </button>
    )
  };
};

const domContainer = document.querySelector('#burger');
ReactDOM.render(el(Burger), domContainer);
