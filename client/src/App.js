import React, { useState } from "react"
import axios from 'axios'


const App = () => {
  const [input, setInput] = useState('')
  
  const onSubmit = (e) => {
    e.preventDefault()
    console.log(input)

    axios.get(`http://localhost:8000/search?query=${input}`,)
      .then(res => {
        console.log(res);
        console.log(res.data);
      })

    setInput('')
  }
  
  return(
    <div>
      <form onSubmit={onSubmit}>
        <label>
          Search:
          <input type="text" name="name" value={input} onChange={(e) => setInput(e.target.value)}/>
        </label>
        <input type="submit" value="Submit" />
      </form>
    </div>
  )
}

export default App;
