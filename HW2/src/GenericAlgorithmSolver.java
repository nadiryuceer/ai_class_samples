import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Random;

public class GenericAlgorithmSolver {
    private static final double mutationRate = 0.1;
    private static final int tournamentSize = 5;
    private static final boolean elitism = true;

    public static RouteManager evolveRoute(RouteManager routes) {

        Route best = routes.findBestFitness();
        int loc = 0;
        Route temp = crossover(routes.getRoute(0),routes.getRoute(routes.getLength()-1));
        for(int i=0;i<routes.getLength()-1;i++){
            routes.setRoute(i,crossover(routes.getRoute(i),routes.getRoute(i+1)));
        }
        routes.setRoute(routes.getLength()-1,temp);
        for(int i=0;i<routes.getLength();i++){
            mutate(routes.getRoute(i));
        }
        RouteManager newroutes = new RouteManager(50,false);
        RouteManager chosen = new RouteManager(tournamentSize,false);
        for(int i=0;i<50;i++) {
            for (int j = 0; j < chosen.getLength(); j++) {
                chosen.setRoute(j, routes.getRoute((int) (Math.random() * 49)));
            }
            newroutes.setRoute(i, tournamentSelection(chosen));
        }
        if(elitism){
            temp = routes.getRoute(0);
            for(int i=1;i<routes.getLength();i++) {
                if (routes.getRoute(i).getFitness() < temp.getFitness()) loc = i;
            }
            routes.setRoute(loc, best);
        }
        routes=newroutes;
        return routes; // for avoiding error"
    }

    public static Route crossover(Route parent1, Route parent2) {
        Route newroute = new Route();
        int dividerf = (int)(Math.random()*19);
        int dividerl = (int)(Math.random()*19);
        while(dividerl==dividerf){
            dividerl = (int)(Math.random()*19);
        }
        if(dividerf>dividerl){
            int temp = dividerf;
            dividerf = dividerl;
            dividerl = temp;
        }
        int loc=dividerf;
        int fill=dividerl;
        int init=0;
        while(loc<dividerl){
            newroute.setCity(loc,parent1.getCity(loc));
            loc++;
        }
        while(loc!=dividerl||init==0){
            for(int i=dividerf;i<dividerl;i++){
                if(parent2.getCity(loc)==newroute.getCity(i)){
                    break;
                }
                if(i==dividerl-1){
                    newroute.setCity(fill,parent2.getCity(loc));
                    fill++;
                }
            }
            loc++;
            init = 1;
            if(loc==parent2.getLength()) loc=0;
            if(fill==parent2.getLength()) fill=0;
        }

        return newroute; // for avoiding error
    }

    private static void mutate(Route route) {
        if(Math.random()<=mutationRate) {
            // RestrictedMutation
            City temp;
            int rcl = (int) (Math.random() * 19);
            int rcr = (int) (Math.random() * 19);
            if (rcl != rcr) {
                temp = route.getCity(rcl);
                route.setCity(rcl, route.getCity(rcr));
                route.setCity(rcr, temp);
            }
        }
    }

    private static Route tournamentSelection(RouteManager routes) {
        // YOUR CODE HERE
        return routes.findBestFitness(); // for avoiding error
    }



}
