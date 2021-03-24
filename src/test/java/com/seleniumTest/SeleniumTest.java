package com.seleniumTest;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import org.openqa.selenium.WebDriver;

import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;



public class SeleniumTest {
    WebDriver dr;
    seleniumWithJava swj;

    @BeforeEach
    public void setUp(){
        dr=new ChromeDriver();
        swj=new seleniumWithJava(dr);
    }

    @Test
    public void SeleniumRun(){
        String url="http://www.amazon.com";
        String expectedTitle="Java: The Complete Reference, Eleventh "+
                "Edition: Schildt, Herbert: 9781260440232: Amazon.com: Books";
        String actualTitle;
        actualTitle=swj.seleniumRun(url,"java","The Complete Reference");
        assertEquals(expectedTitle,actualTitle);
    }

    @AfterEach
    public void tearDown(){
        swj.tearDown();
    }
}
