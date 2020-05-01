class SmallestMultiple {

    public static void main(String[] args) {
        /*
            2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
            What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
        */


        int smallest = Integer.MAX_VALUE;
        int max = Integer.MAX_VALUE;
        int range = 20;

        for(int i = 1; i < max; i++){

            for(int j = 1; j <= range; j++){
                if(i % j == 0 && j != range){
                    continue;
                }else if(i % j == 0 && j == range){
                    if(i < smallest){
                        smallest = i;
                    }
                }else{
                    break;
                }
            }
        }

        System.out.print(smallest);
    }
}
