package com.raynor.geek.springbootapp.redis

import org.springframework.context.annotation.Bean
import org.springframework.context.annotation.Configuration
import org.springframework.data.redis.connection.RedisConnectionFactory
import org.springframework.data.redis.core.RedisTemplate
import org.springframework.data.redis.serializer.StringRedisSerializer

@Configuration
class RedisConfig {

//    @Bean
//    fun connectionFactory(): LettuceConnectionFactory {
//        return LettuceConnectionFactory(
//            RedisStandaloneConfiguration().apply {
//                this.database = 0
//                this.hostName = "localhost"
//                this.port = 6379
//            }
//        )
//    }

    @Bean
    fun redisTemplate(
        connectionFactory: RedisConnectionFactory,
    ): RedisTemplate<String, String> {
        return RedisTemplate<String, String>().apply {
            this.connectionFactory = connectionFactory
            this.keySerializer = StringRedisSerializer()
            this.valueSerializer = StringRedisSerializer()
            this.setEnableTransactionSupport(true)
        }
    }
}