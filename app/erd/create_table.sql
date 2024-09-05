CREATE TABLE public.tb_sample (
	sp_id varchar NULL, -- id
	sp_nm varchar NULL, -- 이름
	crt_usr varchar NULL, -- 생성자id
	crt_dttm timestamp NULL DEFAULT CURRENT_TIMESTAMP -- 생성일시
);
COMMENT ON TABLE public.tb_sample IS '샘플 테이블';
COMMENT ON COLUMN public.tb_sample.sp_id IS 'id';
COMMENT ON COLUMN public.tb_sample.sp_nm IS '이름';
COMMENT ON COLUMN public.tb_sample.crt_usr IS '생성자id';
COMMENT ON COLUMN public.tb_sample.crt_dttm IS '생성일시';

CREATE TABLE public.tb_sample_history (
	svc_cd varchar NOT NULL, -- 서비스구분
	usr_id varchar NOT NULL, -- 사용자id
	usr_ip varchar NULL, -- 사용자ip
	usr_dept varchar NULL, -- 사용자부서
	usr_url varchar NOT NULL, -- 사용자접근url
	usr_param varchar NULL, -- 사용자파리미터
	crt_dttm timestamp NULL DEFAULT CURRENT_TIMESTAMP -- 생성일시
);
COMMENT ON TABLE public.tb_sample_history IS '사용자 사용 이력';
COMMENT ON COLUMN public.tb_sample_history.svc_cd IS '서비스구분';
COMMENT ON COLUMN public.tb_sample_history.usr_id IS '사용자id';
COMMENT ON COLUMN public.tb_sample_history.usr_ip IS '사용자ip';
COMMENT ON COLUMN public.tb_sample_history.usr_dept IS '사용자부서';
COMMENT ON COLUMN public.tb_sample_history.usr_url IS '사용자접근url';
COMMENT ON COLUMN public.tb_sample_history.usr_param IS '사용자파리미터';
COMMENT ON COLUMN public.tb_sample_history.crt_dttm IS '생성일시';