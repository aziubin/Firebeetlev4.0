
int __hallRead()    //hall sensor using idf read
{
    pinMode(36, ANALOG);
    pinMode(39, ANALOG);
    __analogSetWidth(12);
    return hall_sensor_read();
}
