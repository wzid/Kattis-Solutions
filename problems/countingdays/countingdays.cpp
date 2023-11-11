

int last = 0;
int day = 1;

void lookAtClock(int hours, int minutes) {
    if ((hours*60) + minutes < last) {
        day++;
        last = (hours*60) + minutes;
    }else if ((hours*60) + minutes > last) {
        last = (hours*60) + minutes;
    }
}

int getDay() {
    return day;
}
