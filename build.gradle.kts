import org.jetbrains.kotlin.gradle.tasks.KotlinCompile
import com.google.protobuf.gradle.*

val protobufVersion = "3.25.3"
// setting this to match lemon-pi
val grpcVersion = "1.57.0"

plugins {
    idea
    `java-library`
    kotlin("jvm")
    id("com.google.protobuf") version "0.9.4"
    `maven-publish`
}

group = "com.normtronix"
version = "1.4"
java.sourceCompatibility = JavaVersion.VERSION_11


repositories {
    mavenCentral()
}

tasks.withType<KotlinCompile> {
    kotlinOptions {
        freeCompilerArgs = listOf("-Xjsr305=strict")
        jvmTarget = "11"
    }
}

dependencies {

    implementation("org.jetbrains.kotlin:kotlin-stdlib")
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.5.2")
    implementation("io.grpc:grpc-protobuf:${grpcVersion}")
    implementation("io.grpc:grpc-stub:${grpcVersion}")
    implementation("io.grpc:grpc-kotlin-stub:1.2.0")
    implementation("com.google.protobuf:protobuf-java:${protobufVersion}")
    compileOnly("jakarta.annotation:jakarta.annotation-api:1.3.5") // Java 9+ compatibility - Do NOT update to 2.0.0
}

protobuf {
    protoc {
        artifact = "com.google.protobuf:protoc:${protobufVersion}"
    }
    plugins {
        id("grpc") {
            artifact = "io.grpc:protoc-gen-grpc-java:${grpcVersion}"
        }
        id ("grpckt") {
            artifact = "io.grpc:protoc-gen-grpc-kotlin:1.2.0:jdk7@jar"
        }
    }
    generateProtoTasks {
        all().forEach {
            it.plugins {
                id("grpc")
                id("grpckt")
            }
        }
    }
}

java {
    withSourcesJar()
    withJavadocJar()
}

publishing {
    publications {
        create<MavenPublication>("maven") {
            from(components["java"])
            
            pom {
                name.set("Lemon Pi Protos")
                description.set("Protocol Buffer definitions for the Lemon Pi racing telemetry system")
                url.set("https://github.com/sprintf/lemon-pi-protos")
                
                licenses {
                    license {
                        name.set("MIT License")
                        url.set("https://opensource.org/licenses/MIT")
                    }
                }
                
                developers {
                    developer {
                        id.set("sprintf")
                        name.set("Paul Normington")
                        email.set("paul@normingtons.org")
                    }
                }
                
                scm {
                    connection.set("scm:git:git://github.com/sprintf/lemon-pi-protos.git")
                    developerConnection.set("scm:git:ssh://github.com:sprintf/lemon-pi-protos.git")
                    url.set("https://github.com/sprintf/lemon-pi-protos/tree/master")
                }
            }
        }
    }
    
    repositories {
        maven {
            name = "GitHubPackages"
            url = uri("https://maven.pkg.github.com/sprintf/lemon-pi-protos")
            credentials {
                username = System.getenv("GITHUB_ACTOR")
                password = System.getenv("GITHUB_TOKEN")
            }
        }
    }
}

