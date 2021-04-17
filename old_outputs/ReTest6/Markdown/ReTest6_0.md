
# Parameters

    Name :                      ReTest6-0
    Main :                      CFagentv2
    Level :                     Levels.Causal3
    Failed actions chance :     0.0
    Hours :                     12.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        2000000.0
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        500000.0
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
    Layer greendown :           True
    Layer greenup :             True
    Layer greenstar :           True
    Layer yellowstar :          True
    Layer bluestar :            True
    Layer coconut :             True
    Layer monster :             True
    Layer greencross :          True
    Layer bluecross :           True
    Layer redcross :            True
    Layer purplecross :         True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                4
    Counterfacts :              1
    Topn :                      5
    Random counterfacts :       True
    Minutes used :              715 minutes.
    Hours used :                11 hours.

# Profiling


      26606590221 function calls (26479389671 primitive calls) in 42918.19 seconds

##    Ordered by: cumulative time
   List reduced from 523 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42918.190 42918.190 {built-in method builtins.exec}
                      1    7.451    7.451 42918.190 42918.190 <string>:1(<module>)
                      1  220.016  220.016 42910.739 42910.739 main.py:105(CFagentv2)
                4424736   23.013    0.000 12165.280    0.003 agent.py:29(learn)
                4422008  316.815    0.000 9707.167    0.002 learner.py:42(Qlearn)
                1474912    9.149    0.000 8053.776    0.005 game.py:41(step)
                1474912   10.476    0.000 7686.578    0.005 layers.py:718(step)
        144934027/17735261  681.672    0.000 5521.589    0.000 module.py:866(_call_impl)
               11838342  171.734    0.000 4927.049    0.000 container.py:117(forward)
                1474912  153.307    0.000 4881.131    0.003 layers.py:17(step)
                1474912  217.297    0.000 4746.925    0.003 agent.py:54(_learn)
              147126937  275.926    0.000 4712.265    0.000 layer.py:98(move)
               10344727   32.906    0.000 4572.148    0.000 network.py:24(forward)
                5896919   63.533    0.000 4506.960    0.001 optimizer.py:84(wrapper)
                1474912  208.850    0.000 4326.944    0.003 agent.py:202(_learn)
                5896919   34.572    0.000 4238.862    0.001 grad_mode.py:24(decorate_context)
                5896919  200.386    0.000 4135.659    0.001 adam.py:55(step)
                5896919  857.614    0.000 3725.145    0.001 _functional.py:53(adam)
                1474912 3207.903    0.002 3638.941    0.002 replaybuffer.py:85(sample_data)
                5896919   29.958    0.000 3285.662    0.001 tensor.py:195(backward)
                1474912  494.880    0.000 3277.781    0.002 agent.py:236(counterfact2)
                5896919   31.642    0.000 3254.610    0.001 __init__.py:68(backward)
                5896919 3084.264    0.001 3084.264    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                1474912   54.745    0.000 3057.013    0.002 agent.py:117(_learn)
                1474912 2423.555    0.002 2987.583    0.002 replaybuffer.py:22(sample_data)
                1474912   30.291    0.000 2796.638    0.002 simulator.py:50(learn)
                1474913  236.193    0.000 2777.745    0.002 layers.py:684(update)
                1474912  215.245    0.000 2766.347    0.002 simulator.py:23(learn)
              147126937  569.070    0.000 2746.277    0.000 layers.py:735(check)
                1474912 2007.526    0.001 2575.085    0.002 replaybuffer.py:52(sample_data)
                2956919  108.956    0.000 2245.218    0.001 agent.py:49(__call__)
               25170299   62.332    0.000 1991.885    0.000 conv.py:398(forward)
               20051242 1948.975    0.000 1948.975    0.000 {built-in method tensor}
               25170299   45.483    0.000 1895.940    0.000 conv.py:390(_conv_forward)
               16638224   12.030    0.000 1852.821    0.000 game.py:37(board)
               25170299 1850.458    0.000 1850.458    0.000 {built-in method conv2d}
               23598600 1033.733    0.000 1834.991    0.000 layer.py:167(NoRock_update)
                1474912  735.756    0.000 1822.505    0.001 agent.py:88(interveen)
              147126937  261.060    0.000 1464.486    0.000 layers.py:729(isFree)
                1474912  815.892    0.001 1389.924    0.001 replaybuffer.py:28(teleporter_save_data)
               28084357   64.953    0.000 1257.930    0.000 linear.py:93(forward)
                1474912  817.853    0.001 1243.553    0.001 agent.py:67(modify)
               25085659 1213.693    0.000 1213.693    0.000 {built-in method cat}
             1075955804 1023.389    0.000 1203.426    0.000 layer.py:95(isFree)
               28084357   26.509    0.000 1156.480    0.000 functional.py:1737(linear)
               28084357 1123.643    0.000 1123.643    0.000 {built-in method torch._C._nn.linear}
                1472184   36.655    0.000  786.805    0.001 agent.py:171(__call__)
                1474912  643.427    0.000  775.169    0.001 replaybuffer.py:91(simulator_save_data)
              100239444  720.847    0.000  720.847    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                1474912   35.068    0.000  701.612    0.000 agent.py:112(__call__)
               41416314   42.212    0.000  697.636    0.000 activation.py:713(forward)
               63402847  697.419    0.000  697.419    0.000 {built-in method clone}
                1873893   21.777    0.000  666.769    0.000 layers.py:740(restart)
                4431831   39.538    0.000  666.634    0.000 agent.py:59(modify_board)
                5896919  125.106    0.000  662.460    0.000 optimizer.py:189(zero_grad)
               41416314   42.363    0.000  655.424    0.000 functional.py:1364(leaky_relu)
                1474912  508.949    0.000  654.095    0.000 replaybuffer.py:58(CF_save_data)
              100239444  634.777    0.000  634.777    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              147126937  413.130    0.000  607.556    0.000 layers.py:246(check)
               41416314  605.167    0.000  605.167    0.000 {built-in method torch._C._nn.leaky_relu}
                5925446  599.575    0.000  599.575    0.000 {built-in method torch._C._nn.one_hot}
             2146784985  404.240    0.000  586.227    0.000 enum.py:646(__hash__)
              147092320  137.712    0.000  581.645    0.000 {built-in method builtins.any}
              147126937  321.818    0.000  509.918    0.000 layers.py:286(check)
                1493615    7.816    0.000  494.749    0.000 simulator.py:20(boardforward)
              453699555  490.975    0.000  490.975    0.000 layer.py:146(elements)
                1873893   11.016    0.000  476.166    0.000 level.py:8(__init__)
                1472184   35.787    0.000  445.239    0.000 replaybuffer.py:48(stacker)
             1310556663  368.474    0.000  443.933    0.000 layers.py:700(<genexpr>)
                1474912   31.782    0.000  434.029    0.000 replaybuffer.py:18(stacker)
               50119722  421.258    0.000  421.258    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                8172522  161.224    0.000  409.933    0.000 random.py:315(sample)
               50119722  380.768    0.000  380.768    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                1873893   47.173    0.000  369.573    0.000 levels.py:164(generate)
               50119722  347.453    0.000  347.453    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               50119722  346.475    0.000  346.475    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                5896919   11.703    0.000  316.456    0.000 loss.py:527(forward)
              350838144  254.385    0.000  314.277    0.000 tensor.py:906(grad)
                5896919   33.648    0.000  304.754    0.000 functional.py:2898(mse_loss)
              147491300   46.596    0.000  304.392    0.000 {built-in method builtins.all}
                1474911   27.934    0.000  304.131    0.000 replaybuffer.py:81(stacker)
              475606595  129.860    0.000  277.371    0.000 layers.py:690(<genexpr>)
        3313359130/3313359126  240.948    0.000  273.850    0.000 {built-in method builtins.len}
              147126937  176.016    0.000  271.782    0.000 layers.py:273(check)
                3747786   36.384    0.000  266.622    0.000 level.py:41(notUsed)
              147126937  172.676    0.000  262.053    0.000 layers.py:313(check)
             2628672493  256.809    0.000  256.809    0.000 layer.py:91(positions)
               50119722  253.906    0.000  253.906    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                2956919   82.368    0.000  249.529    0.000 exploration.py:53(softmaxer)
                1474912  140.096    0.000  231.322    0.000 collector.py:46(collect)
              147126937  158.244    0.000  226.239    0.000 layers.py:48(check)
               14699650  209.643    0.000  209.643    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                1474912   38.426    0.000  208.279    0.000 agent.py:277(counterfact_check)
                4820226  192.308    0.000  192.308    0.000 {built-in method nonzero}
                5896919  185.150    0.000  185.150    0.000 {built-in method torch._C._nn.mse_loss}
             2146802188  181.991    0.000  181.991    0.000 {built-in method builtins.hash}
              255751811  121.449    0.000  181.079    0.000 random.py:250(_randbelow_with_getrandbits)
              147126937  114.543    0.000  171.311    0.000 layers.py:23(check)
               70800477  163.379    0.000  163.379    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               14991144   21.727    0.000  163.359    0.000 layer.py:69(restart)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-12>
Subject: Job 9512497: <ReTest6_0> in cluster <dcc> Done

Job <ReTest6_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Apr 13 13:40:47 2021
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue Apr 13 21:24:27 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Apr 13 21:24:27 2021
Terminated at Wed Apr 14 09:19:52 2021
Results reported at Wed Apr 14 09:19:52 2021

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

    CPU time :                                   42600.86 sec.
    Max Memory :                                 6810 MB
    Average Memory :                             5044.25 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               9574.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42926 sec.
    Turnaround time :                            70745 sec.

The output (if any) is above this job summary.

