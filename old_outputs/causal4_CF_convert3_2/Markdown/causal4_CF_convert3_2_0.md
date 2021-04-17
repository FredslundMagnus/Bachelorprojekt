
# Parameters

    Name :                      causal4_CF_convert3_2-0
    Main :                      CFagent
    Level :                     Levels.Causal4
    Hours :                     24.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        1000000
    Learner2 :                  Learners.Qlearn
    Exploration2 :              Explorations.epsilonGreedy
    Gamma2 :                    0.95
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    Layer reddoor :             True
    Layer redkeys :             True
    Layer bluedoor :            True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      57348077278 function calls (57040175147 primitive calls) in 86115.28 seconds

##    Ordered by: cumulative time
   List reduced from 508 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86115.278 86115.278 {built-in method builtins.exec}
                      1    5.128    5.128 86115.278 86115.278 <string>:1(<module>)
                      1  316.279  316.279 86110.150 86110.150 main.py:96(CFagent)
                9956205   60.342    0.000 27729.040    0.003 agent.py:29(learn)
                9956202  725.662    0.000 22189.969    0.002 learner.py:42(Qlearn)
                3318735   20.658    0.000 19392.212    0.006 game.py:35(step)
                3318735   22.536    0.000 18482.580    0.006 layers.py:448(step)
        344621257/36720817 1551.539    0.000 12670.919    0.000 module.py:866(_call_impl)
                3318735  334.843    0.000 12543.949    0.004 layers.py:17(step)
              331873500  931.922    0.000 12177.260    0.000 layer.py:84(move)
               26764615   84.939    0.000 11741.068    0.000 network.py:24(forward)
               26764615  388.087    0.000 11454.772    0.000 container.py:117(forward)
                3318735  971.917    0.000 11390.592    0.003 agent.py:204(counterfact)
                3318735  461.273    0.000 10840.984    0.003 agent.py:54(_learn)
                3318735  448.868    0.000 9714.776    0.003 agent.py:196(_learn)
                9956202  121.115    0.000 8372.924    0.001 optimizer.py:84(wrapper)
                9956202   65.799    0.000 7851.329    0.001 grad_mode.py:24(decorate_context)
                9956202  368.941    0.000 7646.337    0.001 adam.py:55(step)
                3318735  123.994    0.000 7085.562    0.002 agent.py:115(_learn)
              331873500 1079.425    0.000 6966.781    0.000 layers.py:465(check)
                9956202 1598.122    0.000 6891.075    0.001 _functional.py:53(adam)
                3318735 5302.451    0.002 6642.904    0.002 replaybuffer.py:22(sample_data)
                8400840  308.228    0.000 6379.091    0.001 agent.py:49(__call__)
                9956202   54.961    0.000 6025.184    0.001 tensor.py:195(backward)
                9956202   57.956    0.000 5968.655    0.001 __init__.py:68(backward)
                3318736  415.968    0.000 5876.560    0.002 layers.py:419(update)
               52568225 5789.654    0.000 5789.654    0.000 {built-in method tensor}
                9956202 5649.471    0.001 5649.471    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3318735 4460.580    0.001 5618.671    0.002 replaybuffer.py:49(sample_data)
               44929308   34.153    0.000 5576.488    0.000 game.py:31(board)
               66374710 3181.636    0.000 5426.735    0.000 layer.py:129(update)
                3318735 2702.921    0.001 4670.978    0.001 replaybuffer.py:28(teleporter_save_data)
                3318735 2034.722    0.001 4489.979    0.001 agent.py:86(interveen)
               53529230  134.770    0.000 4394.924    0.000 conv.py:398(forward)
               53529230  106.032    0.000 4193.059    0.000 conv.py:390(_conv_forward)
               53529230 4087.027    0.000 4087.027    0.000 {built-in method conv2d}
              331795870  633.951    0.000 3640.022    0.000 layers.py:459(isFree)
               73656375  160.125    0.000 3189.521    0.000 linear.py:93(forward)
             2848354427 2543.769    0.000 3006.071    0.000 layer.py:81(isFree)
               73656375   65.222    0.000 2943.160    0.000 functional.py:1737(linear)
               73656375 2863.088    0.000 2863.088    0.000 {built-in method torch._C._nn.linear}
                1770106   44.159    0.000 2617.735    0.001 agent.py:168(choose_action)
                3318735 1481.376    0.000 2569.107    0.001 agent.py:67(modify)
               48225645 2024.788    0.000 2024.788    0.000 {built-in method cat}
              179876569 1883.079    0.000 1883.079    0.000 {built-in method clone}
               11719575  103.292    0.000 1825.900    0.000 agent.py:59(modify_board)
                3318732   75.744    0.000 1723.316    0.001 agent.py:164(__call__)
              100420990   94.955    0.000 1640.502    0.000 activation.py:713(forward)
                3318735   73.043    0.000 1550.141    0.000 agent.py:110(__call__)
              100420990   97.067    0.000 1545.547    0.000 functional.py:1364(leaky_relu)
             5750781253 1084.948    0.000 1531.860    0.000 enum.py:646(__hash__)
              100420990 1431.013    0.000 1431.013    0.000 {built-in method torch._C._nn.leaky_relu}
             1136220459 1380.978    0.000 1380.978    0.000 layer.py:124(elements)
              185849100 1321.007    0.000 1321.007    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              331873600  155.674    0.000 1262.940    0.000 {built-in method builtins.all}
                3334383   44.523    0.000 1203.519    0.000 layers.py:469(restart)
               11719575 1201.858    0.000 1201.858    0.000 {built-in method torch._C._nn.one_hot}
                9956202  218.441    0.000 1188.849    0.000 optimizer.py:189(zero_grad)
              331873500  774.601    0.000 1185.305    0.000 layers.py:233(check)
              185849100 1170.746    0.000 1170.746    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             1669581241  446.557    0.000 1149.053    0.000 layers.py:425(<genexpr>)
              331873500  666.271    0.000 1095.100    0.000 layers.py:270(check)
                3318735   91.130    0.000 1037.801    0.000 replaybuffer.py:18(stacker)
              331873500  807.800    0.000 1036.709    0.000 layers.py:67(check)
                3318732   81.886    0.000  868.375    0.000 replaybuffer.py:45(stacker)
                3334383   21.596    0.000  815.308    0.000 level.py:8(__init__)
                3318735  326.008    0.000  805.600    0.000 replaybuffer.py:55(CF_save_data)
              331873500  615.119    0.000  779.735    0.000 layers.py:56(check)
               92924550  772.732    0.000  772.732    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             7943087550  740.476    0.000  740.476    0.000 layer.py:77(positions)
               92924550  698.711    0.000  698.711    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                8400840  239.717    0.000  692.474    0.000 exploration.py:53(softmaxer)
                3334383  117.737    0.000  654.794    0.000 levels.py:199(generate)
               92924550  650.037    0.000  650.037    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               92924550  648.377    0.000  648.377    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               13306236  243.479    0.000  638.130    0.000 random.py:315(sample)
              331873600  431.210    0.000  622.728    0.000 layers.py:100(isDone)
        8175526423/8175526420  541.780    0.000  616.254    0.000 {built-in method builtins.len}
              331873500  402.874    0.000  612.648    0.000 layers.py:294(check)
              331873500  383.321    0.000  590.333    0.000 layers.py:257(check)
              650471934  466.470    0.000  575.932    0.000 tensor.py:906(grad)
                9956202   23.581    0.000  573.411    0.000 loss.py:527(forward)
                9956202   59.425    0.000  549.830    0.000 functional.py:2898(mse_loss)
                3318735  312.773    0.000  535.926    0.000 collector.py:54(collect)
                9956206  501.241    0.000  501.241    0.000 {built-in method nonzero}
              331873500  336.925    0.000  492.730    0.000 layers.py:42(check)
                1770106  421.493    0.000  480.164    0.000 agent.py:179(convert_values)
               92924550  453.884    0.000  453.884    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             5750819028  446.919    0.000  446.919    0.000 {built-in method builtins.hash}
              194914876  425.602    0.000  425.602    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                6668766   53.250    0.000  419.294    0.000 level.py:41(notUsed)
              310024654  247.376    0.000  352.997    0.000 layer.py:104(remove)
               33343830   50.197    0.000  332.486    0.000 layer.py:58(restart)
              502789475  232.558    0.000  324.895    0.000 layer.py:108(add)
                9956202  319.993    0.000  319.993    0.000 {built-in method torch._C._nn.mse_loss}
               66374710  308.979    0.000  308.979    0.000 layer.py:141(<listcomp>)
              408945599  206.688    0.000  307.912    0.000 random.py:250(_randbelow_with_getrandbits)
                9957373  294.854    0.000  294.854    0.000 {built-in method max}
               15045043   33.132    0.000  276.035    0.000 tensor.py:525(__rsub__)
               53529230   44.986    0.000  273.313    0.000 flatten.py:39(forward)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-12>
Subject: Job 9496008: <causal4_CF_convert3_2_0> in cluster <dcc> Done

Job <causal4_CF_convert3_2_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon Apr  5 20:00:35 2021
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Apr  5 21:12:11 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr  5 21:12:11 2021
Terminated at Tue Apr  6 21:07:34 2021
Results reported at Tue Apr  6 21:07:34 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   85895.71 sec.
    Max Memory :                                 9831 MB
    Average Memory :                             6517.15 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6553.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86123 sec.
    Turnaround time :                            90419 sec.

The output (if any) is above this job summary.

