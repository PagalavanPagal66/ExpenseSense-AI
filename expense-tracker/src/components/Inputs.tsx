import { useState , useReducer } from "react";
import './Inputs.css'

const Inputs = () => {

    const [expenseList,setExpenseList] = useState<{expense :string , amount:number , date : Date}[]>([]);
    const [expenseName,setTask] = useState("");
    const [expenseAmt, setAmt] = useState(0);
    const [expenseDate, setDate] = useState(new Date());

    const addtask = () => {
        const newExpenseName : string = expenseName;
        const newExpenseAmt : number = expenseAmt;
        const newExpenseDate : Date = expenseDate;
        const newobject = 
        {
            expense : newExpenseName,
            amount : newExpenseAmt,
            date : newExpenseDate
        }  
        setExpenseList([...expenseList,newobject]);
        setTask("");
        setAmt(0);
    }
    
    const updateExpenseName = (e : React.ChangeEvent<HTMLInputElement>) => {
        setTask(e.target.value);
    }

    const updateExpenseAmt = (e : React.ChangeEvent<HTMLInputElement>) => {
        setAmt(+e.target.value);
    }

    const updateDate = () => {
        let currDate : Date = new Date();
        setDate(currDate);
    }

    const deleteExpense = (index : number) => {
        setExpenseList(expenseList.filter(
            (element :{expense:string , amount:number , date : Date} ,i : number) => i!==index
        ))
    }

    return(
        <div className = "main-div">
            <input className="input" type="text" value = {expenseName} placeholder="Enter expense name" onChange={updateExpenseName}/>
            <input type="number" placeholder="Enter expense amount" onChange={updateExpenseAmt}/>
            <button onClick={addtask}>Submit</button>
            <h1>{expenseName}</h1>
            <ol className="order-list">
                {expenseList.map(
                    (currExpense :{expense:string , amount:number , date : Date} ,index : number) =>    
                            <li className = {"doneclass"} key={index} id={index.toString()}>
                                <span>{currExpense.expense + "   " + currExpense.amount + " " + currExpense.date}</span>
                            </li>
                )}
            </ol>   
        </div>
    )
}
export default Inputs;