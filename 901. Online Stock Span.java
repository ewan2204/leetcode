class StockSpanner {
    private ArrayList<Integer> yesterdayStock;

    public StockSpanner() {
        yesterdayStock = new ArrayList<Integer>();
    }
    
    public int next(int price) {
        yesterdayStock.add(price);
        int span = 0;
        for(int i = yesterdayStock.size()-1; i >= 0; i--){
            if(yesterdayStock.get(i) <= price){
                span++;
            }else{
                break;
            }
        }
        return span;
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner obj = new StockSpanner();
 * int param_1 = obj.next(price);
 */
