let myFunction = (event)=>{
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const dateOfBirth = document.getElementById('dob').value;
    let dateOfSubscription = new Date().toLocaleDateString("es-CL");
    let myNewCustomer = {};
  
    myNewCustomer['name'] = name
    myNewCustomer['email'] = email
    myNewCustomer['date_of_birth'] = dateOfBirth
    myNewCustomer['date_of_subscription'] = dateOfSubscription
    
    fetch("receiver", 
    {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            'Accept': 'application/json',
        },
        body: JSON.stringify(myNewCustomer)
    }).then(res => {
        if(res.ok){
            return res.json()
        }else{
            alert('Wrong!!')
        }
    }).then(jsonResponse => {
        document.getElementById('notification').innerHTML = '<div class="column is-half"><div class="notification is-success is-light">New Customer has been successfuly created</div></div>'
        console.log(jsonResponse)
    }).catch((err) =>console.error(err));
}