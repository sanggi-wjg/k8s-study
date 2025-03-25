package com.raynor.geek.springbootapp.utils

import java.math.BigDecimal

fun factorial(n: Int): BigDecimal {
    require(n >= 0) { "Factorial is not defined for negative numbers." }

    var result = BigDecimal.ONE
    for (i in 2..n) {
        result = result.multiply(BigDecimal(i))
    }
    return result
}