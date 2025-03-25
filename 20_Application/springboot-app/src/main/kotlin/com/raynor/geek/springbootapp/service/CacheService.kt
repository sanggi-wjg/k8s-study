package com.raynor.geek.springbootapp.service

import com.raynor.geek.springbootapp.controller.dto.CacheResponseDto
import org.springframework.data.redis.core.RedisTemplate
import org.springframework.stereotype.Service
import java.util.concurrent.TimeUnit
import kotlin.random.Random

@Service
class CacheService(
    private val redisTemplate: RedisTemplate<String, String>
) {

    fun simpleGetOrSet(): CacheResponseDto {
        val rand = Random.nextInt(1, 100)
        val key = "simple-key:$rand"

        val value = redisTemplate.opsForValue().get(key) ?: run {
            redisTemplate.opsForValue().set(key, rand.toString(), 60, TimeUnit.SECONDS)
            rand.toString()
        }
        return CacheResponseDto(key, value.toInt())
    }
}

