const API_URL="http://localhost:8000"

export const fetchTransactions=async()=>{
    const res=await fetch($`{API_URL}/transactions/`);
    return res.json();
};

export const createTransaction=async(data)=>{
    const res=await fetch(`${API_URL}/transactions/`,{
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify(data)
    });
    return res.json();
};
export const fetchTransaction = async(id)=>{
   await fetch(`${API_URL}/transactions/${id}`,{method:"DELETE"});
};

export const fetchSummary=async () =>{
    const res=await fetch(`${API_URL}/summary`);
    return res.json();
};

export const fetchCategoryBreakdown = async () =>{
    const res=await fetch(`${API_URL}/category-breakdown`);
    return res.json();
};


