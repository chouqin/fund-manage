BEGIN;
CREATE TABLE `funds_department` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(32) NOT NULL
)
;
CREATE TABLE `funds_teacher` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(10) NOT NULL,
    `title` varchar(32) NOT NULL,
    `department_id` integer NOT NULL,
    `is_dean` bool NOT NULL
)
;
ALTER TABLE `funds_teacher` ADD CONSTRAINT `department_id_refs_id_39f8397e` FOREIGN KEY (`department_id`) REFERENCES `funds_department` (`id`);
CREATE TABLE `funds_projecttype` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(32) NOT NULL
)
;
CREATE TABLE `funds_project_teachers` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `project_id` integer NOT NULL,
    `teacher_id` integer NOT NULL,
    UNIQUE (`project_id`, `teacher_id`)
)
;
ALTER TABLE `funds_project_teachers` ADD CONSTRAINT `teacher_id_refs_id_2484c27f` FOREIGN KEY (`teacher_id`) REFERENCES `funds_teacher` (`id`);
CREATE TABLE `funds_project` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `project_type_id` integer NOT NULL,
    `name` varchar(64) NOT NULL,
    `created_at` datetime NOT NULL,
    `ended_at` datetime NOT NULL
)
;
ALTER TABLE `funds_project` ADD CONSTRAINT `project_type_id_refs_id_372c4af` FOREIGN KEY (`project_type_id`) REFERENCES `funds_projecttype` (`id`);
ALTER TABLE `funds_project_teachers` ADD CONSTRAINT `project_id_refs_id_768b91b8` FOREIGN KEY (`project_id`) REFERENCES `funds_project` (`id`);
CREATE TABLE `funds_device` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(64) NOT NULL,
    `specification` varchar(32) NOT NULL,
    `maker` varchar(32) NOT NULL,
    `is_import` bool NOT NULL,
    `price` double precision NOT NULL,
    `amount` integer NOT NULL,
    `remain_amount` integer NOT NULL,
    `position` varchar(32) NOT NULL,
    `usage` varchar(64) NOT NULL,
    `year` datetime NOT NULL,
    `project_id` integer NOT NULL
)
;
ALTER TABLE `funds_device` ADD CONSTRAINT `project_id_refs_id_205173eb` FOREIGN KEY (`project_id`) REFERENCES `funds_project` (`id`);
CREATE TABLE `funds_business` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `total` double precision NOT NULL,
    `remain` double precision NOT NULL,
    `year` datetime NOT NULL,
    `project_id` integer NOT NULL
)
;
ALTER TABLE `funds_business` ADD CONSTRAINT `project_id_refs_id_29710863` FOREIGN KEY (`project_id`) REFERENCES `funds_project` (`id`);
CREATE TABLE `funds_deviceexpense` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `device_id` integer NOT NULL,
    `amount` integer NOT NULL,
    `created_at` datetime NOT NULL,
    `status` integer NOT NULL,
    `teacher_id` integer NOT NULL
)
;
ALTER TABLE `funds_deviceexpense` ADD CONSTRAINT `teacher_id_refs_id_46167d3b` FOREIGN KEY (`teacher_id`) REFERENCES `funds_teacher` (`id`);
ALTER TABLE `funds_deviceexpense` ADD CONSTRAINT `device_id_refs_id_223c257c` FOREIGN KEY (`device_id`) REFERENCES `funds_device` (`id`);
CREATE TABLE `funds_businessexpense` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `business_id` integer NOT NULL,
    `amount` double precision NOT NULL,
    `created_at` datetime NOT NULL,
    `status` integer NOT NULL,
    `teacher_id` integer NOT NULL
)
;
ALTER TABLE `funds_businessexpense` ADD CONSTRAINT `teacher_id_refs_id_279b7a93` FOREIGN KEY (`teacher_id`) REFERENCES `funds_teacher` (`id`);
ALTER TABLE `funds_businessexpense` ADD CONSTRAINT `business_id_refs_id_39cb3aac` FOREIGN KEY (`business_id`) REFERENCES `funds_business` (`id`);
COMMIT;
