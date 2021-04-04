
# Parameters

    Name :                      NOBUGcausal4_CFagent_convert0-0
    Main :                      CFagent
    Level :                     Levels.Causal4
    Hours :                     16.0
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
    Layer reddoors :            True
    Layer redkeys :             True
    Layer bluedoors :           True
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
    Cf convert :                0
    Minutes used :              955 minutes.
    Hours used :                15 hours.

# Profiling


      35010770470 function calls (34826178539 primitive calls) in 57318.05 seconds

##    Ordered by: cumulative time
   List reduced from 493 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 57318.047 57318.047 {built-in method builtins.exec}
                      1    4.746    4.746 57318.047 57318.047 <string>:1(<module>)
                      1  145.631  145.631 57313.301 57313.301 main.py:96(CFagent)
                6007644   23.098    0.000 19460.379    0.003 agent.py:28(learn)
                6007641  485.819    0.000 16248.948    0.003 learner.py:42(Qlearn)
                2002548   10.667    0.000 11343.207    0.006 game.py:36(step)
                2002548   13.117    0.000 10831.677    0.005 layers.py:594(step)
        206647917/22057677  918.242    0.000 8216.997    0.000 module.py:866(_call_impl)
               16050036   46.678    0.000 7702.606    0.000 network.py:24(forward)
               16050036  240.180    0.000 7548.038    0.000 container.py:117(forward)
                2002548  221.819    0.000 7510.805    0.004 agent.py:53(_learn)
                2002548  185.126    0.000 7314.402    0.004 layers.py:18(step)
              200254800  468.316    0.000 7111.134    0.000 layer.py:82(move)
                2002548  814.719    0.000 7078.613    0.004 agent.py:199(counterfact)
                2002548  218.294    0.000 6952.454    0.003 agent.py:191(_learn)
                6007641   53.449    0.000 6917.378    0.001 optimizer.py:84(wrapper)
                6007641   27.614    0.000 6651.204    0.001 grad_mode.py:24(decorate_context)
                6007641  189.862    0.000 6562.720    0.001 adam.py:55(step)
                6007641 1361.285    0.000 6156.710    0.001 _functional.py:53(adam)
                2002548 3063.763    0.002 5709.819    0.003 replaybuffer.py:28(teleporter_save_data)
                2002548   63.290    0.000 4960.713    0.002 agent.py:114(_learn)
              200254800  644.416    0.000 4295.433    0.000 layers.py:611(check)
                6007641   27.257    0.000 4043.733    0.001 tensor.py:195(backward)
                6007641   24.892    0.000 4015.440    0.001 __init__.py:68(backward)
                2002548 2383.254    0.001 3942.544    0.002 agent.py:85(interveen)
                5019889  142.097    0.000 3916.185    0.001 agent.py:48(__call__)
                6007641 3845.742    0.001 3845.742    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               32567935 3494.102    0.000 3494.102    0.000 {built-in method tensor}
                2002549  232.214    0.000 3486.571    0.002 layers.py:565(update)
               27830125   20.795    0.000 3347.220    0.000 game.py:32(board)
                2002548 2285.616    0.001 3059.402    0.002 replaybuffer.py:22(sample_data)
               32100072   79.899    0.000 2706.369    0.000 conv.py:398(forward)
               40050970 1585.168    0.000 2694.814    0.000 layer.py:127(update)
               32100072   44.731    0.000 2591.539    0.000 conv.py:390(_conv_forward)
               32100072 2546.808    0.000 2546.808    0.000 {built-in method conv2d}
                2002548 1805.965    0.001 2482.637    0.001 replaybuffer.py:49(sample_data)
              171439928 2379.813    0.000 2379.813    0.000 {built-in method clone}
               44145012   98.591    0.000 2185.038    0.000 linear.py:93(forward)
              200246336  372.980    0.000 2045.006    0.000 layers.py:605(isFree)
               44145012   41.375    0.000 2039.717    0.000 functional.py:1737(linear)
               44145012 1988.544    0.000 1988.544    0.000 {built-in method torch._C._nn.linear}
                1017413   11.421    0.000 1766.935    0.002 agent.py:167(choose_action)
                2002548 1015.631    0.001 1684.113    0.001 agent.py:66(modify)
             1678160238 1326.072    0.000 1672.025    0.000 layer.py:79(isFree)
              112142628 1251.962    0.000 1251.962    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               29050450 1249.106    0.000 1249.106    0.000 {built-in method cat}
               60195048   50.892    0.000 1218.753    0.000 activation.py:713(forward)
               60195048   55.128    0.000 1167.861    0.000 functional.py:1364(leaky_relu)
              112142628 1104.625    0.000 1104.625    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               60195048 1101.475    0.000 1101.475    0.000 {built-in method torch._C._nn.leaky_relu}
                7022437   52.736    0.000 1090.352    0.000 agent.py:58(modify_board)
                2002545   36.758    0.000 1081.225    0.001 agent.py:163(__call__)
                2002548   34.812    0.000 1025.738    0.001 agent.py:109(__call__)
                6007641  155.480    0.000  962.622    0.000 optimizer.py:189(zero_grad)
                2782136   31.600    0.000  940.759    0.000 layers.py:615(restart)
             3394139682  654.425    0.000  939.295    0.000 enum.py:646(__hash__)
              200254900  104.333    0.000  818.252    0.000 {built-in method builtins.all}
              200254800  472.915    0.000  764.988    0.000 layers.py:303(check)
             1082485567  296.619    0.000  739.517    0.000 layers.py:571(<genexpr>)
              200254800  422.159    0.000  711.173    0.000 layers.py:262(check)
                7022437  691.976    0.000  691.976    0.000 {built-in method torch._C._nn.one_hot}
                2002548  296.552    0.000  687.799    0.000 replaybuffer.py:55(CF_save_data)
               56071314  684.672    0.000  684.672    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              804318069  640.040    0.000  640.040    0.000 layer.py:122(elements)
                2782136   15.142    0.000  632.575    0.000 level.py:8(__init__)
                2002548   53.588    0.000  621.416    0.000 replaybuffer.py:18(stacker)
              200254800  472.145    0.000  610.512    0.000 layers.py:76(check)
               56071314  604.226    0.000  604.226    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              180464910  603.636    0.000  603.636    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               56071314  569.469    0.000  569.469    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               56071314  562.835    0.000  562.835    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
             5009060148  534.265    0.000  534.265    0.000 layer.py:75(positions)
                2782136   92.284    0.000  529.925    0.000 levels.py:199(generate)
                2002545   48.253    0.000  529.071    0.000 replaybuffer.py:45(stacker)
              200254800  346.271    0.000  461.405    0.000 layers.py:63(check)
                2002548  269.599    0.000  446.999    0.000 collector.py:54(collect)
                1017413  389.470    0.000  445.064    0.000 agent.py:178(convert_values)
               56071314  436.581    0.000  436.581    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                5019889  149.015    0.000  409.329    0.000 exploration.py:53(softmaxer)
              200254800  242.910    0.000  388.740    0.000 layers.py:329(check)
        4379146299/4379146296  315.311    0.000  357.189    0.000 {built-in method builtins.len}
              392499282  284.513    0.000  355.268    0.000 tensor.py:906(grad)
              200254800  220.048    0.000  352.346    0.000 layers.py:288(check)
                5564272   41.079    0.000  350.694    0.000 level.py:41(notUsed)
              200254900  223.960    0.000  338.768    0.000 layers.py:111(isDone)
                9569368  125.266    0.000  329.749    0.000 random.py:315(sample)
                6007641    9.356    0.000  314.903    0.000 loss.py:527(forward)
              200254800  196.715    0.000  306.811    0.000 layers.py:47(check)
                6007641   25.634    0.000  305.547    0.000 functional.py:2898(mse_loss)
                6007645  285.083    0.000  285.083    0.000 {built-in method nonzero}
             3394162785  284.874    0.000  284.874    0.000 {built-in method builtins.hash}
               27821360   38.302    0.000  267.076    0.000 layer.py:56(restart)
              196658155  176.473    0.000  236.602    0.000 layer.py:102(remove)
              363222634  155.400    0.000  210.599    0.000 layer.py:106(add)
               32100072   24.003    0.000  202.172    0.000 flatten.py:39(forward)
                6007641  200.657    0.000  200.657    0.000 {built-in method torch._C._nn.mse_loss}
             1339530534  189.037    0.000  189.037    0.000 layer.py:183(isBlocking)
               12015288  188.805    0.000  188.805    0.000 {built-in method sum}
              272731149  128.526    0.000  187.859    0.000 random.py:250(_randbelow_with_getrandbits)
                6008342  178.633    0.000  178.633    0.000 {built-in method max}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-13>
Subject: Job 9494241: <NOBUGcausal4_CFagent_convert0_0> in cluster <dcc> Done

Job <NOBUGcausal4_CFagent_convert0_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Apr  4 02:59:53 2021
Job was executed on host(s) <n-62-20-13>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Apr  4 02:59:53 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Apr  4 02:59:53 2021
Terminated at Sun Apr  4 18:55:26 2021
Results reported at Sun Apr  4 18:55:26 2021

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

    CPU time :                                   57171.35 sec.
    Max Memory :                                 7026 MB
    Average Memory :                             5267.10 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               9358.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   57383 sec.
    Turnaround time :                            57333 sec.

The output (if any) is above this job summary.

