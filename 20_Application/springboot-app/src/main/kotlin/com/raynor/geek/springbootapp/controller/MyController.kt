package com.raynor.geek.springbootapp.controller

import com.raynor.geek.springbootapp.controller.dto.CacheResponseDto
import com.raynor.geek.springbootapp.service.CacheService
import com.raynor.geek.springbootapp.utils.factorial
import org.springframework.http.ResponseEntity
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.RestController
import kotlin.random.Random

@RestController
class MyController(
    private val cacheService: CacheService,
) {

    @GetMapping("/")
    fun root(): ResponseEntity<String> {
        return ResponseEntity.ok("Hello world")
    }

    @GetMapping("/factorial")
    fun calc(): ResponseEntity<String> {
        val rand = Random.nextInt(1, 100)
        return ResponseEntity.ok(factorial(rand).toString())
    }

    @GetMapping("/cache")
    fun cache(): ResponseEntity<CacheResponseDto> {
        return ResponseEntity.ok(cacheService.simpleGetOrSet())
    }
}