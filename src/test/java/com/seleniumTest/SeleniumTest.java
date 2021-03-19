package com.seleniumTest;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import org.openqa.selenium.WebDriver;

import org.openqa.selenium.chrome.ChromeDriver;


public class SeleniumTest {
    WebDriver driver;

    @BeforeEach
    public void setUp(){
        driver=new ChromeDriver();
        String url="http://www.amazon.com";
        driver.get(url);
    }

    @Test
    public void SeleniumRun(){
        String expectedTitle="Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more";
        String actualTitle=driver.getTitle();
        assertEquals(expectedTitle,actualTitle);
    }

    @AfterEach
    public void tearDown(){
        driver.close();
    }

}
