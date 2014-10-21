



-- ---
-- Globals
-- ---

-- SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
-- SET FOREIGN_KEY_CHECKS=0;

-- ---
-- Table 'TWEETS'
-- Twitters
-- ---
DROP TABLE IF EXISTS `INCIDENTS`;

DROP TABLE IF EXISTS `TWEETS`;
		
CREATE TABLE `TWEETS` (
  `ID_TWEET` INTEGER(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `TEXT` VARCHAR(255) NULL DEFAULT NULL,
  `CREATED_AT` TIMESTAMP,
  `RETWEETS` INTEGER NULL DEFAULT NULL,
  `ID_USER` VARCHAR(100) NOT NULL,
  `LOCATION` VARCHAR(255) NULL DEFAULT NULL,
  `SOURCE` VARCHAR(100) NULL DEFAULT NULL,
  `COORDINATES` VARCHAR(255) NULL DEFAULT NULL,
  `PLACE` VARCHAR(255) NULL DEFAULT NULL,
  `GEOENABLE` TINYINT(1) DEFAULT 0,
  `ID_TWITTER` VARCHAR(100) NULL DEFAULT NULL,
  PRIMARY KEY (`ID_TWEET`)
) COMMENT 'Twitters';

-- ---
-- Table 'USERS'
-- 
-- ---

DROP TABLE IF EXISTS `USERS`;
		
CREATE TABLE `USERS` (
  `ID_USER` VARCHAR(100) NOT NULL,
  `NAME` VARCHAR(100) NULL DEFAULT NULL,
  `TIMEZONE` VARCHAR(10) NULL DEFAULT NULL,
  `LANGUAGE` VARCHAR(100) NULL DEFAULT NULL,
  `FOLLOWERS` INTEGER NULL DEFAULT NULL,
  `DESCRIPTION` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`ID_USER`)
);

-- ---
-- Table 'INCIDENTS'
-- 
-- ---

DROP TABLE IF EXISTS `INCIDENTS`;
		
CREATE TABLE `INCIDENTS` (
  `ID_INCIDENT` INTEGER(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `ID_TWEET` INTEGER(11) UNSIGNED NOT NULL,
  `ID_ITYPE` INTEGER (11) UNSIGNED NOT NULL,
  PRIMARY KEY (`ID_INCIDENT`)
);

-- ---
-- Table 'INCIDENT_TYPE'
-- 
-- ---

DROP TABLE IF EXISTS `INCIDENT_TYPE`;
		
CREATE TABLE `INCIDENT_TYPE` (
  `ID_ITYPE` INTEGER(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `ITYPE_DESC` VARCHAR(40) NOT NULL,
  PRIMARY KEY (`ID_ITYPE`)
);

-- ---
-- Foreign Keys 
-- ---

ALTER TABLE `TWEETS` ADD FOREIGN KEY (ID_USER) REFERENCES `USERS` (`ID_USER`);
ALTER TABLE `INCIDENTS` ADD FOREIGN KEY (ID_TWEET) REFERENCES `TWEETS` (`ID_TWEET`);
ALTER TABLE `INCIDENTS` ADD FOREIGN KEY (ID_ITYPE) REFERENCES `INCIDENT_TYPE` (`ID_ITYPE`);

-- ---
-- Table Properties
-- ---

ALTER TABLE `TWEETS` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
ALTER TABLE `USERS` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
ALTER TABLE `INCIDENTS` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
ALTER TABLE `INCIDENT_TYPE` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ---
-- Test Data
-- ---

-- INSERT INTO `TWEETS` (`ID_TWEET`,`TEXT`,`CREATED_AT`,`RETWEETS`,`ID_USER`,`LOCATION`,`SOURCE`,`COORDINATES`,`PLACE`,`GEOENABLE`,`ID_TWITTER`,`new field`) VALUES
-- ('','','','','','','','','','','','');
-- INSERT INTO `USERS` (`ID_USER`,`NAME`,`TIMEZONE`,`LANGUAGE`,`FOLLOWERS`,`DESCRIPTION`) VALUES
-- ('','','','','','');
-- INSERT INTO `INCIDENTS` (`ID_INCIDENT`,`ID_TWEET`,`ID_ITYPE`) VALUES
-- ('','','');
INSERT INTO `INCIDENT_TYPE` (`ID_ITYPE`,`ITYPE_DESC`) VALUES
(1,'ACCIDENTE');

INSERT INTO `INCIDENT_TYPE` (`ID_ITYPE`,`ITYPE_DESC`) VALUES
(2,'TRAFICO');


